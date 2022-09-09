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
	dx := [4]int{1, 1, 0, -1}
	dy := [4]int{0, 1, 1, 1}

	n := NumStdin()
	area := make([]string, n)
	for i := 0; i < n; i++ {
		area[i] = StrStdin()
	}

	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			for k := 0; k < 4; k++ {
				var tgt, cnt int
				for m := 0; m < 6; m++ {
					nx, ny := i+dx[k]*m, j+dy[k]*m
					if nx < 0 || nx >= n || ny < 0 || ny >= n {
						continue
					}

					tgt++

					if string(area[nx][ny]) == "#" {
						cnt++
					}
				}
				if tgt == 6 && cnt >= 4 {
					fmt.Println("Yes")
					return
				}
			}
		}
	}

	fmt.Println("No")
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
