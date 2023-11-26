from hypothesis import given, strategies as st
from hypothesis.extra.pandas import data_frames, column

import buckaroo

SUPPORTED_DATA = st.one_of(st.integers(), st.floats(), st.text(), st.dictionaries(st.text(), st.integers()),
                           st.lists(st.text()))


# TODO: replace st.nothing() with appropriate strategies


@given(
    # TODO: write strategy to support n-Columns
    df=st.one_of(data_frames(columns=[column(elements=SUPPORTED_DATA)]),
                 data_frames(columns=[column(elements=SUPPORTED_DATA), column(elements=SUPPORTED_DATA)]),
                 data_frames(columns=[column(elements=SUPPORTED_DATA), column(elements=SUPPORTED_DATA),
                                      column(elements=SUPPORTED_DATA)]),
                 ),
    sampled=st.booleans(),
    summaryStats=st.booleans(),
    reorderdColumns=st.booleans(),
    showCommands=st.booleans(),
    auto_clean=st.booleans(),
    postProcessingF=st.none(),
    debug=st.booleans(),
)
def test_fuzz_BuckarooWidget(
        df,
        sampled,
        summaryStats,
        reorderdColumns,
        showCommands,
        auto_clean,
        postProcessingF,
        debug,
):
    buckaroo.BuckarooWidget(
        df=df,
        sampled=sampled,
        summaryStats=summaryStats,
        reorderdColumns=reorderdColumns,
        showCommands=showCommands,
        auto_clean=auto_clean,
        postProcessingF=postProcessingF,
        debug=debug,
    )

#
# @given(ser=st.nothing())
# def test_fuzz_get_typing_metadata(ser):
#     buckaroo.get_typing_metadata(ser=ser)
#
#
# @given(type_dict=st.nothing())
# def test_fuzz_recommend_type(type_dict):
#     buckaroo.recommend_type(type_dict=type_dict)
