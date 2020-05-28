package vuongdx.constraint;

import localsearch.model.*;

public class ConstraintSystemWrapper extends AbstractInvariant implements IFunction {

    private IConstraint cs;
    private VarIntLS[] _variables;

    public ConstraintSystemWrapper(IConstraint cs) {
        this.cs = cs;
        this._variables = cs.getVariables();
        cs.getLocalSearchManager().post(this);
    }

    @Override
    public LocalSearchManager getLocalSearchManager() {
        return cs.getLocalSearchManager();
    }

    public void post(IConstraint c) {

        if (cs instanceof ConstraintSystem) {
            ((ConstraintSystem) cs).post(c);
        }
    }

    @Override
    public int getMinValue() {
        return Integer.MIN_VALUE;
    }

    @Override
    public int getMaxValue() {
        return Integer.MAX_VALUE;
    }

    @Override
    public int getValue() {
        return cs.violations();
    }

    public int violations() {
        return cs.violations();
    }

    public int violations(VarIntLS x) {
        return cs.violations(x);
    }

    @Override
    public int getAssignDelta(VarIntLS x, int val) {
        return cs.getAssignDelta(x, val);
    }

    @Override
    public int getSwapDelta(VarIntLS x, VarIntLS y) {
        return cs.getSwapDelta(x, y);
    }

    @Override
    public void initPropagate() {

//        cs.initPropagate();
    }

    @Override
    public void propagateInt(VarIntLS x, int val) {

//        cs.propagateInt(x, val);
    }

    @Override
    public VarIntLS[] getVariables() {
        return cs.getVariables();
    }
}
