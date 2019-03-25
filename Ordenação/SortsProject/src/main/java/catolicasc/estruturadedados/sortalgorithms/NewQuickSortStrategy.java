package catolicasc.estruturadedados.sortalgorithms;

/**
 * Ordena usando o método quicksort
 *
 * javarevisited.blogspot.com/2016/09/iterative-quicksort-example-in-java-without-recursion.html#ixzz5i0V1Fj00
 * http://www.sonic.net/~jddarcy/Research/cs339-quicksort.pdf
 * http://www.java67.com/2014/07/quicksort-algorithm-in-java-in-place-example.html
 * https://algs4.cs.princeton.edu/23quicksort/Quick3way.java.html
 *
 * @author Glauco Vinicius Scheffel
 */
public class NewQuickSortStrategy extends AbstractSortStrategy {
	/**
	 * Implementa a ordenação pelo método
	 */
	@Override
	public void sort() {
		final int[] data = this.getElements();
		quickSort(data, 0, data.length - 1);
	}

	private static void quickSort(final int[] input, int startIdx, int endIdx) {
		int idx = partition(input, startIdx, endIdx);

		if (startIdx < idx - 1) {
			quickSort(input, startIdx, idx - 1);
		}
		if (endIdx > idx) {
			quickSort(input, idx, endIdx);
		}
	}

	private static int partition(int[] input, int start, int end) {
		int piv = input[start];

		while (start <= end) {
			while (input[start] < piv) {
				start++;
			}
			while (input[end] > piv) {
				end--;
			}

			if (start <= end) {
				swap(input, start, end);

				start++;
				end--;
			}
		}
		return start;
	}

	private final static void swap(int[] arr, int i, int j) {
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}

	@Override
	public String toString() {
		return "NewQuickSort";
	}
}
