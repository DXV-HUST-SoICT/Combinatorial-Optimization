package vuongdx.search;

import java.util.HashMap;

import localsearch.model.IFunction;
import localsearch.model.VarIntLS;

public interface ISelectMoveLS {

	public IMoveLS select(IFunction f,
						  HashMap<String, VarIntLS[]> dVar,
						  IMoveLS[] moveList,
						  IMoveLS[] legalMoveList);

}