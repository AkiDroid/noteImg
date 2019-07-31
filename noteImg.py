import tkinter
from PIL import Image
from tkinter import filedialog


def on_click_confirm(msg, str_file_name, width, quality, display_fn):
    file_name = str_file_name.get()
    try:
        img = Image.open(file_name)
    except:
        msg.set('选择文件错误')
        return
    if quality > 95 or quality < 1:
        msg.set('quality错误')
        return
    size = img.size
    if width > size[0]:
        msg.set('尺寸错误')
        return
    opt_size = (width, int(width / size[0] * size[1]))
    img = img.resize(opt_size, Image.ANTIALIAS)
    save_name = file_name.replace('.jpg', '-w{}-q{}.jpg'.format(width, quality))
    img.save(save_name, optimize=True, quality=quality)
    msg.set('OK')
    str_file_name.set('')
    display_fn.set('')


def choose_file(file_name, str_display_fn):
    fn = filedialog.askopenfile()
    file_name.set(fn.name)
    str_display_fn.set(fn.name.split('/')[-1])


def main():
    window = tkinter.Tk()

    str_msg = tkinter.StringVar()
    str_file_name = tkinter.StringVar()
    str_display_fn = tkinter.StringVar()
    str_width = tkinter.StringVar()
    str_width.set(1200)
    str_quality = tkinter.StringVar()
    str_quality.set(50)

    msg_filename = tkinter.Label(window, textvariable=str_display_fn, bg='#e5e5e5', fg='black', width=50, height=2)
    msg_label = tkinter.Label(window, textvariable=str_msg, bg='#e5e5e5', fg='black', width=50, height=2)
    lb_width = tkinter.Label(window, text='width')
    lb_quality = tkinter.Label(window, text='quality')
    entry_width = tkinter.Entry(window, textvariable=str_width, show=None)
    entry_quality = tkinter.Entry(window, textvariable=str_quality, show=None)
    btn_choose = tkinter.Button(
        window, text='选择', width=10, height=2,
        command=lambda: choose_file(str_file_name, str_display_fn)
    )
    btn_confirm = tkinter.Button(
        window, text='确定', width=10, height=2,
        command=lambda: on_click_confirm(
            str_msg, str_file_name, int(str_width.get()), int(str_quality.get()), str_display_fn
        )
    )

    msg_filename.pack()
    msg_label.pack()
    lb_width.pack()
    entry_width.pack()
    lb_quality.pack()
    entry_quality.pack()

    btn_choose.pack()
    btn_confirm.pack()

    window.mainloop()


if __name__ == '__main__':
    main()
