from gooey import Gooey, GooeyParser


# https://chriskiehl.com/article/gooey-as-a-universal-frontend

@Gooey(target="ffmpeg", program_name='Frame Extraction v1.0', suppress_gooey_flag=True, language="Chinese", menu=[{
    'name': 'File',
    'items': [{
        'type': 'AboutDialog',
        'menuTitle': 'About',
        'name': 'Gooey Layout Demo',
        'description': 'An example of Gooey\'s layout flexibility',
        'version': '1.2.1',
        'copyright': '2018',
        'website': 'https://github.com/chriskiehl/Gooey',
        'developer': 'http://chriskiehl.com/',
        'license': 'MIT'
    }, {
        'type': 'MessageDialog',
        'menuTitle': 'Information',
        'caption': 'My Message',
        'message': 'I am demoing an informational dialog!'
    }, {
        'type': 'Link',
        'menuTitle': 'Visit Our Site',
        'url': 'https://github.com/chriskiehl/Gooey'
    }]
}, {
    'name': 'Help',
    'items': [{
        'type': 'Link',
        'menuTitle': 'Documentation',
        'url': 'https://www.readthedocs.com/foo'
    }]
}])
def main():
    parser = GooeyParser(description="Extracting frames from a movie using FFMPEG")
    ffmpeg = parser.add_argument_group('Frame Extraction Util')
    ffmpeg.add_argument('-i',
                        metavar='Input Movie',
                        help='The movie for which you want to extract frames',
                        widget='FileChooser')
    ffmpeg.add_argument('output',
                        metavar='Output Image',
                        help='Where to save the extracted frame',
                        widget='FileSaver',
                        )
    ffmpeg.add_argument('-ss',
                        metavar='Timestamp',
                        help='Timestamp of snapshot (in seconds)')
    ffmpeg.add_argument('-frames:v',
                        metavar='Timestamp',
                        default=1,
                        gooey_options={'visible': False})

    parser.parse_args()


if __name__ == '__main__':
    main()
