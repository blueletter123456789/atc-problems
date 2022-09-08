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
	M = 998244353
)

func init() {
	buf := make([]byte, initBufSize)
	scan.Buffer(buf, maxBufSize)
	scan.Split(bufio.ScanWords)
}

func main() {
	n := NumStdin()
	a := make([]int, n)
	for i := range a {
		a[i] = NumStdin()
	}
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, 10)
	}

	dp[0][a[0]] = 1
	for i := 1; i < n; i++ {
		for j := 0; j < 10; j++ {
			dp[i][(j+a[i])%10] += dp[i-1][j]
			dp[i][(j+a[i])%10] %= M
			dp[i][(j*a[i])%10] += dp[i-1][j]
			dp[i][(j*a[i])%10] %= M
		}
	}

	for _, num := range dp[n-1] {
		fmt.Println(num)
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
