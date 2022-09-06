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
	a, b := NumStdin(), NumStdin()
	c, d := NumStdin(), NumStdin()
	s := ChrStdin()

	dpS := make([]bool, n+1)
	dpF := make([]bool, n+1)

	dpF[b] = true
	for i := b; i < d; i++ {
		if dpF[i] == false {
			continue
		}

		// i+1
		if i < n && string(s[i]) == "." {
			dpF[i+1] = true
		}
		// i+2
		if i+1 < n && string(s[i+1]) == "." {
			dpF[i+2] = true
		}
	}

	dpS[a] = true
	flg := false
	for i := a; i < c; i++ {
		var cnt int

		if dpS[i] == false {
			continue
		}

		if c > d && i >= d && !flg {
			break
		}

		// i+1
		if i < n && string(s[i]) == "." {
			dpS[i+1] = true
			if i >= b-1 {
				cnt++
			}
		}
		// i+2
		if i+1 < n && string(s[i+1]) == "." {
			dpS[i+2] = true
			if i >= b-1 {
				cnt++
			}
		}

		if cnt == 2 {
			flg = true
		}
	}
	
	if dpS[c] && dpF[d] {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}

	// Explanation
	// 1: There is no need to use DP.(i+1||i+2==".")
	// 2: IfC>D, it's NG not empty three in a row.
}

func ChrStdin() string {
	scan.Scan()
	return scan.Text()
}

func NumStdin() int {
	num, err := strconv.Atoi(ChrStdin())
	if err != nil {
		panic(err)
	}
	return num
}
