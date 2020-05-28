package vuongdx.constraint;

import localsearch.model.ConstraintSystem;
import localsearch.model.IFunction;
import localsearch.model.LocalSearchManager;

public class ConstraintSystemFunction extends ConstraintSystem implements IFunction {
    public ConstraintSystemFunction(LocalSearchManager mgr) {
        super(mgr);
    }

    @Override
    public int getMinValue() {
        return this.violations();
    }

    @Override
    public int getMaxValue() {
        return this.violations();
    }

    @Override
    public int getValue() {
        return this.violations();
    }
}
