class ParserFindTagException(Exception):
    """Вызывается, когда парсер не может найти тег."""
    pass


class VersionsListNotFoundError(Exception):
    """Исключение, возникающее, когда не удаётся найти список версий Python."""
    pass
