'text-embedding-ada-002' de facto, is cheaper 98% than their last one.
The same interface is a principle point. 

Pinecone is a bit viral as of this writing and is what people are using. We will be 
using it in this branch.


The basic workflow is:

So overall, the basic behavior would be to take the original prompt of the user, embed it, and do some similarity search and find the relevant documents 
Then simply plug it all to our RAG prompt and sending that to the LLM. And I know right now this looks like magic and we didn't take a look on the implementation of those chains, but trust me, this is what it's doing. And we'll be implementing in the following video the internals of those chains and to see how easy it is to implement it.

Now it's important to note that if we didn't want to use the stuffing strategy, and let's say we wanted to summarize each document before sending it to the LLM, so we could have done that
and we would simply need to put another chain that will do that instead of the combine_docs_chain that we plugged in.



