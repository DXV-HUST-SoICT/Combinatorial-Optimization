package vuongdx.search.solutiongenerator;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;

import localsearch.model.VarIntLS;
import vuongdx.search.ISolutionGeneratorLS;

public class GAllDifferentAllSameRange implements ISolutionGeneratorLS {

	@Override
	public void generateSolution(HashMap<String, VarIntLS[]> dVar) {
		for (String key : dVar.keySet()) {
			VarIntLS[] mVar = dVar.get(key);
			ArrayList<Integer> value = new ArrayList<Integer>();
			for (int i = 0; i < mVar.length; i++) {
				value.add(i);
			}
			Random r = new Random();
			for (int i = 0; i < mVar.length; i++) {
				int idx = r.nextInt(value.size());
				mVar[i].setValuePropagate(mVar[i].getMinValue() + value.get(idx));
				value.remove(idx);
			}
		}
	}

}
