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
	w := NumStdin()
	water := make([]int, 200001)
	for i := 0; i < n; i++ {
		s, t, p := NumStdin(), NumStdin(), NumStdin()
		water[s] += p
		water[t] -= p
	}

	flg := true
	var sum int
	for i := 0; i <= 200000; i++ {
		sum += water[i]
		if sum > w {
			flg = false
			break
		}
	}

	if flg {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
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
