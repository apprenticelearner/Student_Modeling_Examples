#!/bin/bash
FRAC_DIR=../tutors/FractionArithmetic
INT_DIR=../tutors/IntegerArithmetic

python ../utils/gen_training.py -trans_file ds_1190_Study2.txt -agent_type ModularAgent -problem_brds ${FRAC_DIR}/mass_production/mass_production_brds -problem_html ${FRAC_DIR}/HTML/fraction_arithmetic.html -prepost_brds ${FRAC_DIR}/mass_production/pre_test_brds -prepost_html ${FRAC_DIR}/HTML/fraction_arithmetic.html -model_file human_model_values.txt -substep_brds ${FRAC_DIR}/substep -substep_mass_production_template ${INT_DIR}/IntegerArithmetic.brd -substep_html ${INT_DIR}/HTML/IntegerArithmetic.html -iso_brds ${FRAC_DIR}/iso -iso_mass_production_templates ${FRAC_DIR}/mass_production
