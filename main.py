from fuzzer import Fuzzer

# example code
wikipedia_fuzzer = Fuzzer()
wikipedia_fuzzer.fuzz("wikipedia.page", ["String"], 10)
wikipedia_fuzzer.fuzz("wikipedia.summary", ["String"], 10)
wikipedia_fuzzer.fuzz("wikipedia.summary", ["String", "Integer"], 10)

art_fuzzer = Fuzzer()
art_fuzzer.fuzz("tprint", ["String"], 100)

my_fuzzer = Fuzzer()
my_fuzzer.fuzz("my_function", ["String"], 20)