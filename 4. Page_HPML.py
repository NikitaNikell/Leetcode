class Text:

    def __init__(self, text = 'LoL'):
        self.text = text


class Comment(Text):
    def __init__(self, author, text= None):
        super().__init__()
        self.author = author
        self.text = text

    #def __repr__(self):
    #   return str(f'Класс {self.__class__.__name__} унаследован от класса {self.__class__.__bases__}')

    #def __str__(self):
    #    return str(self.author)


class Page:
    def __init__(self, *args):
        self.item = list(args)

    def add_object(self, obj):
        if isinstance(obj, list):
            [self.item.append(i) for i in obj]
        else:
            self.item.append(obj)

    def remove_object(self, obj):
        for i in self.item:
            if obj.__dict__ == i.__dict__:
                self.item.remove(i)
        return

    def __repr__(self):
        return str(self.item)

    def __str__(self):
        #return str([(n, i.__dict__) for n, i in enumerate(self.item, 1)])
        #return '\n'.join(str(x) for x in self.item)
        return '\n'.join(map(str, self.item))


if __name__ == '__main__':
    st = Page(Comment('Nikell'), Text(), Comment('Nikell', 'Hello, World'))
    st.add_object([Comment('st'), Text('TTT')])
    st.add_object(Comment('Black', 'GG, WP'))
    st.remove_object(Comment('Black', 'GG, WP'))
    print(st)
   # [print(i) for i in st]

