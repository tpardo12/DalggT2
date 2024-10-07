public class ProblemaP1 {
    private final Scanner reader = new Scanner(System.in);

    private int[][] buildPyramid(int r, int c) {
        int[][] pyramid = new int[r][c];

        for (int currentRow = 0; currentRow < r; currentRow++) {
            for (int currentCol = 0; currentCol < c; currentCol++) {
                pyramid[currentRow][currentCol] = reader.nextInt();
            }
        }

        return pyramid;
    }

    private int solve(int r, int c) {
        int mid = r >> 1; // Divide by two
        int[][] pyramid = buildPyramid(r, c);

        // The first square will be for Marion and the second will be for Indiana
        int[][][] dp = new int[2][c][c];
        int[][][][] relics = new int[2][c][c][2];

        // Pre-generate all the possible last combination set for all the combinations
        List<int[]>[][] possibleLast = new List[c][c];

        for (int i = 0; i < c; i++) {
            for (int j = 0; j < c; j++) {
                List<int[]> combinations = new ArrayList<>();
                for (int k = -1; k <= 1; k++) {
                    for (int l = -1; l <= 1; l++) {
                        try {
                            int ignored = dp[0][i + k][j + l]; // This will fail when the position is not valid.
                            combinations.add(new int[] { i + k, j + l });
                        } catch (IndexOutOfBoundsException ignored) {
                        }
                    }
                }
                possibleLast[i][j] = combinations;
            }
        }

        int topResult = 0;

        for (int row = 0; row <= mid; row++) {
            int currentIdx = row % 2;
            int prevIdx = (row + 1) % 2;
            // System.err.println("Row " + row);
            for (int i = 0; i < c; i++) { // Marion
                for (int j = 0; j < c; j++) { // Indiana
                    if (row == 0 && (i != c - 1 || j != 0)) {
                        dp[currentIdx][i][j] = Integer.MIN_VALUE;
                        relics[currentIdx][i][j][0] = Integer.MIN_VALUE;
                        relics[currentIdx][i][j][1] = Integer.MIN_VALUE;
                        continue;
                    } else if (row == 0) {
                        dp[currentIdx][i][j] = pyramid[row][i] + pyramid[row][j];
                        relics[currentIdx][i][j][0] = pyramid[row][i];
                        relics[currentIdx][i][j][1] = pyramid[row][j];
                        continue;
                    }

                    // From now row is greater than 0

                    int[] lastCombinationMax = possibleLast[i][j].stream()
                            .map(pos -> new int[] { dp[prevIdx][pos[0]][pos[1]], relics[prevIdx][pos[0]][pos[1]][0],
                                    relics[prevIdx][pos[0]][pos[1]][1] })
                            .max(
                                    Comparator.comparingInt((int[] it) -> it[0]))
                            .orElse(new int[] { Integer.MIN_VALUE, Integer.MIN_VALUE, Integer.MIN_VALUE });

                    relics[currentIdx][i][j][0] = lastCombinationMax[1];
                    relics[currentIdx][i][j][1] = lastCombinationMax[2];

                    // System.err.println(Arrays.deepToString(dp[prevIdx]));
                    // System.err.printf("(%d, %d): %s\n", i, j,
                    // Arrays.toString(lastCombinationMax));

                    if (lastCombinationMax[0] < 0) { // Impossible position or they are death
                        relics[currentIdx][i][j][0] = Integer.MIN_VALUE; // Marion
                        relics[currentIdx][i][j][1] = Integer.MIN_VALUE; // Indiana
                        dp[currentIdx][i][j] = Integer.MIN_VALUE;
                    } else if (i == j && pyramid[row][i] == -1) { // Both are in the same cell and die
                        relics[currentIdx][i][j][0] = Integer.MIN_VALUE; // Marion
                        relics[currentIdx][i][j][1] = Integer.MIN_VALUE; // Indiana
                        dp[currentIdx][i][j] = Integer.MIN_VALUE;
                    } else if (i == j) { // Both are in the same cell, but they do not die
                        dp[currentIdx][i][j] = pyramid[row][i] + lastCombinationMax[0];
                        int playerToAdd = -1;
                        if (lastCombinationMax[1] >= 0)
                            playerToAdd = 0; // Marion
                        else if (lastCombinationMax[2] >= 0)
                            playerToAdd = 1; // Indiana

                        if (playerToAdd != -1) {
                            relics[currentIdx][i][j][playerToAdd] += pyramid[row][i];
                        }
                    } else {
                        int total = lastCombinationMax[0];
                        int deaths = 0;
                        if (pyramid[row][i] == -1) { // Marion dies in this position
                            relics[currentIdx][i][j][0] = Integer.MIN_VALUE;
                            if (lastCombinationMax[1] > 0)
                                total -= lastCombinationMax[1];
                            deaths++;
                        } else if (lastCombinationMax[1] >= 0) { // Still alive
                            total += pyramid[row][i];
                            relics[currentIdx][i][j][0] += pyramid[row][i];
                        }

                        if (pyramid[row][j] == -1) { // Indiana dies in this position
                            relics[currentIdx][i][j][1] = Integer.MIN_VALUE;
                            if (lastCombinationMax[2] > 0)
                                total -= lastCombinationMax[2];
                            deaths++;
                        } else if (lastCombinationMax[2] >= 0) {
                            total += pyramid[row][j];
                            relics[currentIdx][i][j][1] += pyramid[row][j];
                        }

                        dp[currentIdx][i][j] = deaths < 2 ? total : Integer.MIN_VALUE;
                    }
                    // System.err.printf("-> (%d, %d): [%d, %d, %d]\n", i, j, dp[currentIdx][i][j],
                    // relics[currentIdx][i][j][0],relics[currentIdx][i][j][1]);
                }
            }
            topResult = currentIdx;
        }

        int[][] bottom = new int[2][c];
        int sallahStart = c >> 1;

        int finalScore = 0;

        for (int reversedRow = r - 1; reversedRow >= mid; reversedRow--) {
            for (int i = 0; i < c; i++) {
                int currentIdx = reversedRow % 2;
                int prevIdx = (reversedRow + 1) % 2;
                if (reversedRow == r - 1) {
                    bottom[currentIdx][i] = i == sallahStart ? 0 : Integer.MIN_VALUE;
                } else if (reversedRow != mid) {
                    if (pyramid[reversedRow][i] == -1) {
                        bottom[currentIdx][i] = Integer.MIN_VALUE;
                    } else if (c == 1) {
                        bottom[currentIdx][i] = bottom[prevIdx][i] == Integer.MIN_VALUE ? Integer.MIN_VALUE
                                : bottom[prevIdx][i] + pyramid[reversedRow][i];
                    } else if (i == 0) {
                        int prevValue = Math.max(bottom[prevIdx][i], bottom[prevIdx][i + 1]);
                        bottom[currentIdx][i] = prevValue == Integer.MIN_VALUE ? Integer.MIN_VALUE
                                : prevValue + pyramid[reversedRow][i];
                    } else if (i == c - 1) {
                        int prevValue = Math.max(bottom[prevIdx][i], bottom[prevIdx][i - 1]);
                        bottom[currentIdx][i] = prevValue == Integer.MIN_VALUE ? Integer.MIN_VALUE
                                : prevValue + pyramid[reversedRow][i];
                    } else {
                        int prevValue = IntStream.of(bottom[prevIdx][i], bottom[prevIdx][i - 1], bottom[prevIdx][i + 1])
                                .max().getAsInt();
                        bottom[currentIdx][i] = prevValue == Integer.MIN_VALUE ? Integer.MIN_VALUE
                                : prevValue + pyramid[reversedRow][i];
                    }
                } else { // We are ready to find the maximum
                    for (int j = 0; j < c; j++) { // Marion
                        for (int k = 0; k < c; k++) { // Indiana
                            int value = dp[topResult][j][k];
                            if (pyramid[reversedRow][i] != -1 && c != 1) {
                                int prevValue;
                                if (i == 0) {
                                    prevValue = Math.max(bottom[prevIdx][i], bottom[prevIdx][i + 1]);
                                } else if (i == c - 1) {
                                    prevValue = Math.max(bottom[prevIdx][i], bottom[prevIdx][i - 1]);
                                } else {
                                    prevValue = IntStream
                                            .of(bottom[prevIdx][i], bottom[prevIdx][i - 1], bottom[prevIdx][i + 1])
                                            .max().getAsInt();
                                }
                                if (i != j && i != k && prevValue != Integer.MIN_VALUE) {
                                    value += prevValue + pyramid[reversedRow][i];
                                } else if (prevValue != Integer.MIN_VALUE) {
                                    value += prevValue;
                                }
                            }
                            if (value > finalScore)
                                finalScore = value;
                        }
                    }
                }
            }
        }

        return finalScore == 0 ? -1 : finalScore;
    }
}