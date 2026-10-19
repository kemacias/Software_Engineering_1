#Kate Macias
#Software Engineering 1
#Fall 2026
#
# sample class for reference:
# # class Animal:
#     def __init__(self, name):  # <-- The Constructor
#         self.name = name
#         self.leg_count = 4
#
#     def get_leg_count(self):
#         return self.leg_count


class File:
    def __init__(self, file_name):
        self.name = file_name
    def open_file(self, file_name):
        open(self.name)
        return self
    def read_data(self, file_name):
        read(self.name)
        return self
    def write_data(self, file_name, info):
        self.info = info
        self.name = file_name
        write(self.info)
        return self
    def close_file(self, file_name):
        close(self.name)
        return self
