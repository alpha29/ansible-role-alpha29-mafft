def test_mafft(host):
    """
    Check mafft version.
    """
    cmd = "mafft --version"
    cmd_result = host.run(cmd)
    assert cmd_result.rc == 0, "'{}' returned status {}.".format(cmd, cmd_result.rc)
    assert "v7.450 (2019/Aug/23)" in cmd_result.stderr, f"'{cmd}' returned stdout '{cmd_result.stdout}', stderr '{cmd_result.stderr}'"
