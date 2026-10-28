#!/usr/bin/bash
# run_all_tests.sh — batch solution tester
# (see .claude/commands/design-tests.md, section "run_all_tests.sh")
#
# Runs every solution in SOLS against every test set in SETS, one case at a
# time, with language-appropriate time limits. Lives in the problem root;
# run it from there:        bash run_all_tests.sh
#
# Customize SOLS and SETS to match your problem, then comment / uncomment
# lines to scope the run. Keep `python main.py` (regenerate) and this script
# (check) as separate commands for responsiveness.

# Judge time-limit ratios (hard constraint, cannot vary independently):
#   py = 4x cpp, java = 2x cpp
TL_PY=4
TL_JAVA=2
TL_CPP=1

CHECK=./check   # the solution checker, also in the problem root

# Solutions to test — Python first, then Java, then C++ (paths relative to
# the problem root). Comment out anything you don't have or want to skip.
SOLS=(
	"submissions/accepted/sol.py"
	# "submissions/accepted/sol.java"
	# "submissions/accepted/sol.cpp"
)

# Test sets as "setname:glob_pattern"; the glob matches the .in files in that
# set (relative to the problem root). Comment out a set to skip it.
SETS=(
	"sample:data/sample/*.in"
	# "main:data/secret/*_main.in"
	# "bonus1:data/secret/*_bonus1.in"
)

# Expand a glob into the FILES array (empty if nothing matches).
expand_glob() {
	FILES=()
	while IFS= read -r line; do
		FILES+=("$line")
	done < <(compgen -G "$1")
}

for sol in "${SOLS[@]}"; do
	if [[ ! -f "$sol" ]]; then
		echo "[skip] $sol (not found)"
		continue
	fi

	case "$sol" in
		*.py)   tl=$TL_PY   prefix=(PY_CMD=python3) ;;
		*.java) tl=$TL_JAVA prefix=() ;;
		*.cpp)  tl=$TL_CPP  prefix=("CPP_CC=g++ -std=c++17") ;;
		*) echo "[skip] $sol (unknown format)"; continue ;;
	esac

	echo
	echo "######## $sol ########"

	for entry in "${SETS[@]}"; do
		setname=${entry%%:*}
		glob=${entry#*:}
		expand_glob "$glob"
		if (( ${#FILES[@]} == 0 )); then
			echo "[skip] set '$setname' matched no .in files ($glob)"
			continue
		fi
		echo "=== $setname: ${#FILES[@]} case(s) ==="
		for in in "${FILES[@]}"; do
			env "${prefix[@]}" "$CHECK" -t "$tl" -f "$sol" "$in"
		done
	done
done
