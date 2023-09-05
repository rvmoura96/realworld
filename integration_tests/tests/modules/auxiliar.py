def parse_behave_table(context_table):
    """Cast behave's table to a dict."""
    return next(
        dict(zip(context_table.headings, row)) for row in context_table.rows
    )


def cast_table_to_dict(context_table):
    """Cast behave tables into dicts with types."""
    dict_with_strings = parse_behave_table(context_table)
    return dict_with_strings


def cast_table_with_one_column_to_list(context_table):
    """Converte uma tabela com somente uma coluna em uma lista."""
    assert len(context_table.headings), "Tabela com mais de uma coluna"
    return [row[context_table.headings[0]] for row in context_table]
