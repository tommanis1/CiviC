# Example usage:
#   ./regen-funcons.sh 1-Lexical

Sunshine="../../../../dependencies/org.metaborg.sunshine2-2.5.16.jar"
EditorProject="../CIVIC-Editor"

echo "Generating funcons for all .civ files in ./$1"
java -jar ${Sunshine} build --language ${EditorProject} --project "$1" --transform-goal "Generate Funcons" --filter ".*civ"
