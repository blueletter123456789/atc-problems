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
	a := make([]int, n+1)
	same := make([]int, n+1)
	for i := 1; i <= n; i++ {
		a[i] = NumStdin()
		same[i] = same[i-1]
		if i == a[i] {
			same[i]++
		}
	}

	var ans int
	seen := make([]bool, n+1)
	for i := 1; i <= n; i++ {
		if i == a[i] {
			ans += same[n] - same[i]
		} else if  i == a[a[i]] && !seen[i]{
			ans++
			seen[a[i]] = true
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

func min(a, b int) int {
	if a > b {
		return b
	}
	return a
}

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}
