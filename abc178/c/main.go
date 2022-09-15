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
	M = 1_000_000_007
)

func init() {
	buf := make([]byte, initBufSize)
	scan.Buffer(buf, maxBufSize)
	scan.Split(bufio.ScanWords)
}

func main() {
	n := NumStdin()
	allP := powMod(10, n)
	notOtherP := powMod(9, n)
	notP := powMod(8, n)
	ans := allP - notOtherP * 2 + notP
	ans %= M
	fmt.Println((ans+M)%M)
}

func NumStdin() int {
	scan.Scan()
	num, err := strconv.Atoi(scan.Text())
	if err != nil {
		panic(err)
	}
	return num
}

func powMod(a, r int) int {
	p := a
	ret := 1
	for i := 0; i < 60; i++ {
		if r & (1 << i) != 0 {
			ret *= p
			ret %= M
		}
		p *= p
		p %= M
	}
	return ret
}
