class DataTransferObject:
    def __init__(self) -> None:
        self.pages: list[DtoPageData] = []
        self.fonts: list[DtoFontData] = []
        # self.images: list[ImageData] = []


class DtoFontData:
    def __init__(self) -> None:
        self.name: str
        self.raw_data: bytes


class DtoPageData:
    def __init__(self) -> None:
        self.contents: list


class DtoTextArea:
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.paragraphs: list


class DtoParagraph:
    def __init__(
        self,
        width: float,
        height: float,
        line_height_ratio: float,
        tab_size: float,
        first_line_indent: float,
        hanging_indent: float,
        left_indent: float,
        right_indent: float,
        space_before: float,
        space_after: float,
    ) -> None:
        self.width = width
        self.height = height
        self.line_height_ratio = line_height_ratio
        self.tab_size = tab_size
        self.first_line_indent = first_line_indent
        self.hanging_indent = hanging_indent
        self.left_indent = left_indent
        self.right_indent = right_indent
        self.space_before = space_before
        self.space_after = space_after
        self.fragments: list[DtoFragment]


class DtoFragment:
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        baseline: float,
        chars: str,
        font_name: str,
        font_size: float,
        font_color: tuple[int, int, int],
    ) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.baseline = baseline
        self.chars = chars
        self.font_name = font_name
        self.font_size = font_size
        self.font_color = font_color
