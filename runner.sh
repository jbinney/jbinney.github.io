while true
do
  python load_waitlist.py
  git commit -am "Update waitlist"
  git push
done
