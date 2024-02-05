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
        self.paragraphs: list[DtoParagraph] = []
        self.fragments: list[DtoFragment] = []


class DtoParagraph:
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
        self.chars: str = ""
        self.line_height_ratio: float = 0.0
        self.tab_size: float = 0.0
        self.first_line_indent: float = 0.0
        self.hanging_indent: float = 0.0
        self.left_indent: float = 0.0
        self.right_indent: float = 0.0
        self.space_before: float = 0.0
        self.space_after: float = 0.0
        self.text_lines: list[DtoTextLine] = []
        self.fragments: list[DtoFragment] = []

class DtoTextLine:
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
        self.baseline: float = 0.0
        self.space_after: float = 0.0
        self.words: list[DtoWord] = []
        self.fragments: list[DtoFragment] = []

class DtoWord:
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
        self.baseline: float = 0.0
        self.fragments: list[DtoFragment] = []

class DtoFragment:
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
        self.baseline: float = 0.0
        self.chars: str = ""
        self.font_name: str = ""
        self.font_size: float = 0.0
        self.font_color: tuple[int, int, int] = (0, 0, 0)
