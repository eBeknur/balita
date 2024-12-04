class Pagination:
    def __init__(self, objects: list, per_page) -> None:
        self.objects = objects
        self.per_page = per_page
        self.result = self.pagination()
        self.page_count = len(self.result)

    def pagination(self):
        r = []
        for i in range(0, len(self.objects), self.per_page):
            temp = []
            for j in range(i, i + self.per_page):
                if j >= len(self.objects):
                    break
                temp.append(self.objects[j])
            r.append(temp)
        return r

    def get_page(self, page_number: int) -> list:
        if page_number > self.page_count:
            return self.last_page()
        return self.result[page_number - 1]

    def last_page(self):
        return self.result[self.page_count - 1]

    def is_last(self , n):
        if n == self.page_count:
            return True
        return False


    def is_first(self , n):
        if n == 1:
            return True
        return False

