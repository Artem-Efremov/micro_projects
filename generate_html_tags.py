class Tag(object):

    def __init__(self, name, attrs={}, parrent=None):
        self.name = name
        self.attrs = attrs
        if parrent is None:
            self.indent = 0
        else:
            self.indent = parrent.indent + 4

    @property
    def start(self):
        tag = []
        tag.append(self.name)
        if self.attrs:
            for atrr, val in self.attrs.items():
                tag.append('{}="{}"'.format(atrr, val))
        return '{}<{}>'.format(' ' * self.indent, ' '.join(tag))

    @property
    def end(self):
        return '{}</{}>'.format(' ' * self.indent, self.name)

    def __enter__(self):
        print(self.start)
        return self

    def __exit__(self, exc_type, exc, tb):
        print(self.end)
        return self


if __name__ == '__main__':

    with Tag('html', {'lang': 'en'}) as html:

        with Tag('head', {}, html) as head:
            with Tag('title', {}, head) as title:
                offset = (title.indent + 4) * ' '
                print(offset, 'Site')

        with Tag('body', {}, html) as body:
            with Tag('h1', {}, body) as h1:
                offset = (title.indent + 4) * ' '
                print(offset, 'Heading')
            with Tag('div', {'id': 'root', 'class': 'main'}, body) as div:
                offset = (title.indent + 4) * ' '
                print(offset, 'Main content')
