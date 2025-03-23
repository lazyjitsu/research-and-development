$ wget -r -A.html -P langchain-docs https://langchain.readthedocs.io/en/latestwget -r -A.html -P langchain-docs https://langchain.readthedocs.io/en/latest^C


### A note on combine_docs_chain

Now, you might be asking yourself, hey, why do we call it combined docs chain?

And the reason for that is because after we retrieve the relevant documents, we have a lot of options to do and perform optimizations
and to perform actions on the relevant documents, maybe to summarize them, maybe to combine them into one huge string or to do some filtering afterwards. So that's where the combined docs chain is here for. So it gives us also the flexibility to plug in our own functionality for some post-processing after retrieval.