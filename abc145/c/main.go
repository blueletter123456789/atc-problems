package main

import (
	"bufio"
	"fmt"
	"math"
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

type Point struct {
	X, Y float64
}

var dist [][]float64

func main() {
	n := int(NumStdin())
	p := make([]Point, n)
	for i := range p {
		p[i].X, p[i].Y = NumStdin(), NumStdin()
	}

	dist = make([][]float64, n)
	for i := range dist {
		dist[i] = make([]float64, n)
		for j := range dist[i] {
			dist[i][j] = twoDist(p[i], p[j])
		}
	}
	
	var ans float64
	permNum := 1
	for i := 0; i < n; i++ {
		permNum *= (n - i)
		seen := make([]bool, n)
		seen[i] = true
		ans += permutation(i, seen)
	}

	fmt.Println(ans / float64(permNum))
}

func NumStdin() float64 {
	scan.Scan()
	num, err := strconv.ParseFloat(scan.Text(), 64)
	if err != nil {
		panic(err)
	}
	return num
}

func twoDist(a, b Point) float64 {
	x := a.X - b.X
	y := a.Y - b.Y
	return math.Sqrt(x*x + y*y)
}

func permutation(prev int, seen []bool) float64 {

	var sum float64
	for i := range seen {
		if seen[i] {
			continue
		}
		seen[i] = true
		sum += dist[prev][i]
		sum += permutation(i, seen)
		seen[i] = false
	}

	return sum
}
