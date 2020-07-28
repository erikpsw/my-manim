from manimlib.imports import *

class mylatex(Scene):
    def construct(self):
        text1=TexMobject(
            r'''\begin{aligned}
            C &=A B=\left(\begin{array}{ccc}
            1 & 2 & 3 \\
            4 & 5 & 6
            \end{array}\right)\left(\begin{array}{cc}
            1 & 4 \\
            2 & 5 \\
            3 & 6
            \end{array}\right) \\
            &=\left(\begin{array}{cc}
            1 \times 1+2 \times 2+3 \times 3 & 1 \times 4+2 \times 5+3 \times 6 \\
            4 \times 1+5 \times 2+6 \times 3 & 4 \times 4+5 \times 5+6 \times 6
            \end{array}\right) \\
            &=\left(\begin{array}{cc}
            14 & 32 \\
            32 & 77
            \end{array}\right)
            \end{aligned}'''
        )
        self.play(FadeIn(text1))
        self.wait(1)
        self.play(Uncreate(text1))
        A = TextMobject("Text-A").scale(3)
        B = TextMobject("Text-B").scale(3)
        C = TextMobject("C-Text").scale(3)
        self.add(A)
        self.wait()
        self.play(Transform(A, B))
        self.wait()
        self.play(Transform(A, C))
        self.wait()
        self.play(ShrinkToCenter(A))
        A = TextMobject("Text-A").scale(3)
        B = TextMobject("Text-B").scale(3).shift(UP * 2)

        self.add(A)
        self.wait()
        self.play(TransformFromCopy(A, B))
        self.wait()
        mat = np.array([
            [1, 0.5],
            [0, 1]
        ])
        self.play(ApplyMatrix(mat, A))
        mat1=np.array([
            [0.5, 0],
            [0, 0.5],
        ])
        colors = [GRAY, RED, BLUE]
        self.play(FocusOn(A, color=colors))
        self.play(Indicate(B))
        self.play(ApplyMatrix(mat1, B))
        self.play(FadeOutAndShiftDown(A))
        self.wait()
        self.play(FadeOutAndShift(B))