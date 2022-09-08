package main

import (
	"bufio"
	"fmt"
	"os"
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

func main() {
	n := NumStdin()

	minNum := 0
	seen := make(map[int]struct{}, n)
	for i := 0; i < n; i++ {
		p := NumStdin()
		seen[p] = struct{}{}
		for {
			if _, ok := seen[minNum]; ok {
				minNum++
			} else {
				break
			}
		}
		fmt.Println(minNum)
	}
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}
