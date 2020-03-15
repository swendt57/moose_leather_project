# I was trying to adjust the size of photos as part of the model save but ran out of time. Here is what I had working but was unable to integrate it.
# give credit to:
# * Photo adjustment using Pillow - https://auth0.com/blog/image-processing-in-python-with-pillow/
# * Rotation issues - many thanks to all the posts on https://stackoverflow.com/questions/4228530/pil-thumbnail-is-rotating-my-image


THUMB_WIDTH = 400
THUMB_HEIGHT = 300


def adjust_image(request, filename):
    try:

        image = Image.open('products/' + filename)

        if hasattr(image, '_getexif'):  # only present in JPEGs
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break
            e = image._getexif()  # returns None if no EXIF data
            if e is not None:
                exif = dict(e.items())
                orientation = exif[orientation]

                if orientation == 3:
                    image = image.transpose(Image.ROTATE_180)
                elif orientation == 6:
                    image = image.transpose(Image.ROTATE_270)
                elif orientation == 8:
                    image = image.transpose(Image.ROTATE_90)

        image.thumbnail((THUMB_WIDTH, THUMB_HEIGHT), Image.ANTIALIAS)

        new_filename = assemble_new_filename(request, filename)

        image.save('products/' + new_filename)

    except:
        traceback.print_exc()
