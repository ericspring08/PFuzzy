from fuzzer import Fuzzer

wikipedia_fuzzer = Fuzzer()
wikipedia_fuzzer.fuzz("wikipedia.page", ["String"], 10)
wikipedia_fuzzer.fuzz("wikipedia.summary", ["String"], 10)
wikipedia_fuzzer.fuzz("wikipedia.summary", ["String", "Integer"], 10)
wikipedia_fuzzer.print_crash_logs()

art_fuzzer = Fuzzer()
art_fuzzer.fuzz("tprint", ["String"], 100)