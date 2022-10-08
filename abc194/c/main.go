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
	cnt := make([]int, 401)
	for i := 0; i < n; i++ {
		a := NumStdin()
		cnt[a+200]++
	}

	var ans int
	for i := 0; i < 400; i++ {
		for j := i+1; j <= 400; j++ {
			ans += (i-j)*(i-j) * cnt[i] * cnt[j]
		}
	}

	fmt.Println(ans)
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}
