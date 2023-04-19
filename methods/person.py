    def merge_fields(self, other):
        self.alternative_label = "\n".join(filter(None, [self.alternative_label, other.alternative_label]))
        self.gender = self.gender or other.gender
        if self.first_name and other.first_name and self.first_name != other.first_name:
            self.alternative_label += "\n".join(filter(None, [other.first_name, self.alternative_label]))
        self.first_name = self.first_name or other.first_name
        super().merge_fields(other)


