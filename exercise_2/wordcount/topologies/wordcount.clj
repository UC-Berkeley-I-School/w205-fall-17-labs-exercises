(ns wordcount
  (:use     [streamparse.specs])
  (:gen-class))

(defn wordcount [options]
   [
    ;; spout configuration
    {"sentence-spout" (python-spout-spec
          options
          "spouts.sentences.Sentences"
          ["sentence"]
          )
    }
    ;; bolt configuration
    {"sentence-splitter" (python-bolt-spec
          options
          {"sentence-spout" :shuffle}
          "bolts.splitter.SentenceSplitter"
          ["word"]
          :p 2
          )
     "count-bolt" (python-bolt-spec
          options
          {"sentence-splitter" ["word"]}
          "bolts.wordcount.WordCounter"
          ["word" "count"]
          :p 2
          )
    }
  ]
)
