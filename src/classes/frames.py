class frames:
    def __init__(self):
        self.frames = []

    def add_frame(self, frame):
        self.frames.append(frame)

    def __str__(self):
        return f"{self.frames}"

    def __repr__(self):
        return f"{self.frames}"

    def __len__(self):
        return len(self.frames)

    def __getitem__(self, item):
        return self.frames[item]

    def __setitem__(self, key, value):
        self.frames[key] = value
