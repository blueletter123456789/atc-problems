package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var scan = bufio.NewScanner(os.Stdin)

const (
	initBufSize = 10000
	maxBufSize = 10000000
)

type Pair struct {
	N int
	S string
	P int
}

func init() {
	buf := make([]byte, initBufSize)
	scan.Buffer(buf, maxBufSize)
	scan.Split(bufio.ScanWords)
}

func main() {
	n := NumStdin()
	dict := make([]Pair, n)
	for i := range dict {
		dict[i].N = i+1
		dict[i].S = StrStdin()
		dict[i].P = NumStdin()
	}

	sort.Slice(dict, func(i, j int) bool {
		if dict[i].S < dict[j].S {
			return true
		} else if dict[i].S == dict[j].S {
			return dict[i].P > dict[j].P
		}
		return false
	})

	for _, p := range dict {
		fmt.Println(p.N)
	}
}

func StrStdin() string {
	scan.Scan()
	return scan.Text()
}

func NumStdin() int {
	num, err := strconv.Atoi(StrStdin())
	if err != nil {
		panic(err)
	}
	return num
}
