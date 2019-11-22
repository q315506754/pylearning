from gooey import Gooey, GooeyParser
from argparse import ArgumentParser

# cp1251
@Gooey(target="setx", program_name='env path set v1.0', suppress_gooey_flag=True,encoding='gbk')
def main():
    # https://chriskiehl.com/article/gooey-as-a-universal-frontend
    parser = GooeyParser(description="env path set")
    # parser = ArgumentParser(description="My Cool Gooey App!")
    ffmpeg = parser.add_argument_group('argument group')

    # ffmpeg.add_argument('/M',
    #                     metavar='System var',
    #                     default=False,
    #                     required=False,
    #                     widget='CheckBox',
    #                     help='is System var?')

    ffmpeg.add_argument(' ',
                        metavar='var name',
                        default='JAVA_HOME_XX',
                        help='example JAVA_HOME')

    ffmpeg.add_argument(' ',
                        metavar='path',
                        help='example C:\software\\ffmpeg',
                        default='\"C:\software\\ffmpeg\"',
                        # widget='DirChooser'
                        )

    # ffmpeg.add_argument('-i',
    #                     metavar='Input Movie',
    #                     help='The movie for which you want to extract frames',
    #                     widget='FileChooser')
    #
    # ffmpeg.add_argument('output',
    #                     metavar='Output Image',
    #                     help='Where to save the extracted frame',
    #                     widget='FileSaver',
    #                     )
    #
    # ffmpeg.add_argument('-ss',
    #                     metavar='Timestamp',
    #                     help='Timestamp of snapshot (in seconds)')
    #
    # ffmpeg.add_argument('-frames:v',
    #                     metavar='Timestamp',
    #                     default=1,
    #                     gooey_options={'visible': False})

    args = parser.parse_args()

    print(args)
    # display_message()


print()
if __name__ == '__main__':
    main()
