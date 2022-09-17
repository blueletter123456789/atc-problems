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

func main() {
	n := NumStdin()
	cnt := make([]int, n)
	var sumA int
	for i := 0; i < n; i++ {
		a, b := NumStdin(), NumStdin()
		cnt[i] = 2 * a + b
		sumA += a
	}

	sort.Slice(cnt, func(i, j int) bool { return cnt[i] > cnt[j] })

	var sum, ans int
	for i := range cnt {
		sum += cnt[i]
		if sum > sumA {
			ans = i+1
			break
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
