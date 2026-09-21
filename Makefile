.PHONY: foundation analysis audit

foundation:
	cd foundation && lake build --wfail

analysis:
	cd analysis && lake update && lake build --wfail

audit: foundation analysis
	mkdir -p artifacts
	cd foundation && lake env lean RIQGFoundation/Audit.lean | tee ../artifacts/foundation-axioms.txt
	python scripts/check_axioms.py --mode foundation artifacts/foundation-axioms.txt
	cd analysis && lake env lean RIQG/Audit.lean | tee ../artifacts/analysis-axioms.txt
	python scripts/check_axioms.py --mode analysis artifacts/analysis-axioms.txt
