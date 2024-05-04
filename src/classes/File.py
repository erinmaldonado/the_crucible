# 24 fps is the working timecode
from dataclasses import dataclass, field


@dataclass
class File:
    file_path: str
    hp_sans: str = field(default='')  # Assuming this might be needed
    frames_list: list = field(default_factory=list)

    def add(self, frames):
        """Adds frames to the frames_list, frames is expected to be a string of space-separated frame numbers."""
        self.frames_list.extend(frames.split())

    @property
    def ranges(self):
        """Computes and returns ranges based on frames_list. Filters out non-numeric entries."""
        # Filter and convert to integers safely
        valid_frames = []
        for frame in self.frames_list:
            try:
                valid_frames.append(int(frame))
            except ValueError:
                continue  # Skip invalid entries

        if not valid_frames:
            return []

        sorted_frames = sorted(valid_frames)
        ranges = []
        start = sorted_frames[0]
        end = start

        for frame in sorted_frames[1:]:
            if frame == end + 1:
                end = frame
            else:
                ranges.append((start, end))
                start = end = frame
        ranges.append((start, end))
        return ranges

    def to_dict(self):
        """Converts the File object into a dictionary format including dynamically computed ranges."""
        return {
            'HP/SANs': self.hp_sans,
            'File Path': self.file_path,
            'Ranges': self.ranges,  # This will compute ranges
            'Frames': self.frames_list
        }
