package vuongdx.search;

import java.util.HashMap;

import localsearch.model.VarIntLS;

public interface ISolutionGeneratorLS {
	public void generateSolution(HashMap<String, VarIntLS[]> dVar);
}
