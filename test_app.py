"""Smoke test widgets, example loading, target alignment and map selection."""
from streamlit.testing.v1 import AppTest
from physics import preset

at=AppTest.from_file('app.py',default_timeout=30).run()
assert not at.exception
for name in ['Across steps','Along steps','Flat surface','Paper-like L=1.6','Oblique steps']:
    at.selectbox(key='preset_name').select(name).run()
    [b for b in at.button if b.label=='Load example'][0].click().run()
    assert not at.exception, at.exception
    g=preset(name)
    assert at.session_state.phi==g.phi
    assert at.session_state.miscut==g.miscut
    assert at.session_state.energy==g.energy
    print('PASS example:',name)
for layer in ['h','k','l','Intensity']:
    [s for s in at.selectbox if s.label=='Detector colour map'][0].select(layer).run()
    assert not at.exception
print('PASS all detector map modes')
at.number_input(key='target_l').set_value(1.).run()
[b for b in at.button if b.label=='Align sample and detector centre to target'][0].click().run()
assert not at.exception
assert abs(at.session_state.elevation-2*at.session_state.alpha)<1e-10
assert any('captured geometrically' in s.value for s in at.success)
print('PASS target alignment and geometric access')
at.number_input(key='alpha').set_value(-10.).run()
assert not at.exception
assert any('not incident' in s.value for s in at.warning)
print('PASS invalid incidence message')
