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

func init() {
	buf := make([]byte, initBufSize)
	scan.Buffer(buf, maxBufSize)
	scan.Split(bufio.ScanWords)
}

type Score struct {
	num, win int
}

func main() {
	n := NumStdin()
	m := NumStdin()
	
	a := make([]string, n*2)
	rank := make([]*Score, n*2)
	for i := range a {
		a[i] = StrStdin()
		rank[i] = &Score{i, 0}
	}

	for j := 0; j < m; j++ {
		for i := 0; i < n; i++ {
			an, bn := rank[i*2], rank[i*2+1]
			ai, bi := a[an.num][j], a[bn.num][j]
			switch result(string(ai), string(bi)) {
			case 0:
				an.win++
			case 1:
				bn.win++
			}
		}

		sort.Slice(rank, func(ri, rj int) bool { 
			if rank[ri].win == rank[rj].win {
				return rank[ri].num < rank[rj].num
			}
			return rank[ri].win > rank[rj].win })
	}

	for _, p := range rank {
		fmt.Println(p.num+1)
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

func result(a, b string) int {
	if a == b {
		return 2
	}
	if (a=="G"&&b=="C") || (a=="C"&&b=="P")|| (a=="P"&&b=="G") {
		return 0
	}
	return 1
}
