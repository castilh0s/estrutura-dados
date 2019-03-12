import java.util.ArrayList;
import java.util.Random;

public class MergeSort {
	private ArrayList<Integer> inputArray;

	public MergeSort(ArrayList<Integer> inputArray) {
		this.inputArray = inputArray;
	}

	public ArrayList<Integer> getArray() {
		return inputArray;
	}

	public void ordenarArray() {
		dividir(0, this.inputArray.size() - 1);
	}

	public void dividir(Integer indiceInicial, Integer indiceFinal) {
		if (indiceInicial < indiceFinal && (indiceFinal - indiceInicial) >= 1) {
			Integer meio = (indiceFinal + indiceInicial) / 2;
			dividir(indiceInicial, meio);
			dividir(meio + 1, indiceFinal);

			conquistar(indiceInicial, meio, indiceFinal);
		}
	}

	public void conquistar(Integer indiceInicial, Integer indiceMeio, Integer indiceFinal) {
		ArrayList<Integer> mergedSortedArray = new ArrayList<Integer>();

		Integer indiceEsquerdo = indiceInicial;
		Integer indiceDireito = indiceMeio + 1;

		while (indiceEsquerdo <= indiceMeio && indiceDireito <= indiceFinal) {
			if (inputArray.get(indiceEsquerdo) <= inputArray.get(indiceDireito)) {
				mergedSortedArray.add(inputArray.get(indiceEsquerdo));
				indiceEsquerdo++;
			} else {
				mergedSortedArray.add(inputArray.get(indiceDireito));
				indiceDireito++;
			}
		}

		while (indiceEsquerdo <= indiceMeio) {
			mergedSortedArray.add(inputArray.get(indiceEsquerdo));
			indiceEsquerdo++;
		}

		while (indiceDireito <= indiceFinal) {
			mergedSortedArray.add(inputArray.get(indiceDireito));
			indiceDireito++;
		}

		Integer i = 0;
		Integer j = indiceInicial;
		while (i < mergedSortedArray.size()) {
			inputArray.set(j, mergedSortedArray.get(i++));
			j++;
		}
	}

	public static void main(String[] args) throws Exception {
    validate(args);

		Integer TAMANHO = Integer.valueOf(args[0]);
		Integer MAX = Integer.valueOf(args[1]);

		ArrayList<Integer> inputArray = new ArrayList<Integer>();

		Random generator = new Random();
		for (int i = 0; i < TAMANHO; i++) {
			inputArray.add(generator.nextInt(MAX));
		}

		MergeSort ms = new MergeSort(inputArray);

		System.out.println("Array Inicial");
		for (int i : ms.getArray()) {
			System.out.print(i + " ");
		}
		System.out.println();

		ms.ordenarArray();

		System.out.println("\nArray Final");
		for (int i : ms.getArray()) {
			System.out.print(i + " ");
		}
  }

  private static void validate(String[] args) throws Exception {
		if (args.length != 2) {
      throw new Exception("Necessário passar dois valores inteiros como parâmetro:\n01. Tamanho do array;\n02. Valor máximo do array.");
		}
	}
}
