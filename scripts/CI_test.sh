# make and install
set -e
echo "Building...."
./scripts/build_pip.sh
echo "(Done)"

echo "Installing..."
python -m  pip install ./dist/graper-*.whl
echo "(Done)"

# test (is incomplete)
python -m graper example/example.yaml
diff example/graph1.png graph1.png && echo "DIFF TEST: graph1 passed!"
diff example/graph2.png graph2.png && echo "DIFF TEST: graph2 passed!"

# cleaning
echo "Cleaning..."
rm graph1.png graph2.png graph3.png
rm -rf ./dist
echo "(Done)"
# uninstall
echo "Uninstalling..."
python -m pip uninstall -y graper
echo "(Done)"
