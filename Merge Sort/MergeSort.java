import java.util.ArrayList;
import java.util.Random;

public class MergeSort {
	private ArrayList<Integer> inputArray;

	public MergeSort(ArrayList<Integer> inputArray) {
		this.inputArray = inputArray;
	}

	public ArrayList<Integer> getSortedArray() {
		return inputArray;
	}

	public void sortGivenArray() {
		divide(0, this.inputArray.size() - 1);
	}

	public void divide(Integer startIndex, Integer endIndex) {
		if (startIndex < endIndex && (endIndex - startIndex) >= 1) {
			Integer mid = (endIndex + startIndex) / 2;
			divide(startIndex, mid);
			divide(mid + 1, endIndex);

			merger(startIndex, mid, endIndex);
		}
	}

	public void merger(Integer startIndex, Integer midIndex, Integer endIndex) {
		ArrayList<Integer> mergedSortedArray = new ArrayList<Integer>();

		Integer leftIndex = startIndex;
		Integer rightIndex = midIndex + 1;

		while (leftIndex <= midIndex && rightIndex <= endIndex) {
			if (inputArray.get(leftIndex) <= inputArray.get(rightIndex)) {
				mergedSortedArray.add(inputArray.get(leftIndex));
				leftIndex++;
			} else {
				mergedSortedArray.add(inputArray.get(rightIndex));
				rightIndex++;
			}
		}

		while (leftIndex <= midIndex) {
			mergedSortedArray.add(inputArray.get(leftIndex));
			leftIndex++;
		}

		while (rightIndex <= endIndex) {
			mergedSortedArray.add(inputArray.get(rightIndex));
			rightIndex++;
		}

		Integer i = 0;
		Integer j = startIndex;
		while (i < mergedSortedArray.size()) {
			inputArray.set(j, mergedSortedArray.get(i++));
			j++;
		}
	}

	public static void main(String[] args) throws Exception {
    validate(args);

		Integer SIZE = Integer.valueOf(args[0]);
		Integer MAX = Integer.valueOf(args[1]);

		ArrayList<Integer> unsortedArray = new ArrayList<Integer>();

		Random generator = new Random();
		for (int i = 0; i < SIZE; i++) {
			unsortedArray.add(generator.nextInt(MAX));
		}

		MergeSort ms = new MergeSort(unsortedArray);

		System.out.println("Array Inicial");
		for (int i : ms.getSortedArray()) {
			System.out.print(i + " ");
		}
		System.out.println();

		ms.sortGivenArray();

		System.out.println("\nArray Final");
		for (int i : ms.getSortedArray()) {
			System.out.print(i + " ");
		}
  }

  private static void validate(String[] args) throws Exception {
		if (args.length != 2) {
      throw new Exception("Necessário passar dois valores inteiros como parâmetro:\n01. Tamanho do array;\n02. Valor máximo do array.");
		}
	}
}
