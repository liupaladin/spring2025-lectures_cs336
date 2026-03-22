## Progress Tracker (auto-generated)

<!-- PROGRESS-START -->
| User | Progress | L1 | L2 | L3 | L4 | L5 | L6 | L7 | L8 | L9 | L10 | L11 | L12 | L13 | L14 | L15 | L16 | L17 |
|---|---:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| ljx | 6% ▰▱▱▱▱▱▱▱▱▱ | 🟩 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| yj | 0% ▱▱▱▱▱▱▱▱▱▱ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| tg | 0% ▱▱▱▱▱▱▱▱▱▱ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
<!-- PROGRESS-END -->

---

**Landing page:** View the group landing page at [group_landing.html](group_landing.html#L1-L1). It shows the same progress tracker, a collective `questions.md`, and per-user notes in `notes/`.


# Spring 2025 CS336 lectures

This repo contains the lecture materials for "Stanford CS336: Language modeling from scratch".

## Non-executable (ppt/pdf) lectures

Located in `nonexecutable/`as PDFs

## Executable lectures

Located as `lecture_*.py` in the root directory

You can compile a lecture by running:

        python execute.py -m lecture_01

which generates a `var/traces/lecture_01.json` and caches any images as
appropriate.

However, if you want to run it on the cluster, you can do:

        ./remote_execute.sh lecture_01

which copies the files to our slurm cluster, runs it there, and copies the
results back.  You have to setup the appropriate environment and tweak some
configs to make this work (these instructions are not complete).

### Frontend

If you need to tweak the Javascript:

Install (one-time):

        npm create vite@latest trace-viewer -- --template react
        cd trace-viewer
        npm install

Load a local server to view at `http://localhost:5173?trace=var/traces/sample.json`:

        npm run dev

Deploy to the main website:

        cd trace-viewer
        npm run build
        git add dist/assets
        # then commit to the repo and it should show up on the website
