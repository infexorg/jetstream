def pathcalc_om(om1, om2, om3, omd):
    """Calculate the path required to reach a target by anchoring waypoints on
    orbital markers.

    Args:
        om1 (float): Distance in km of closest OM to target.
        om2 (float): Distance in km of 2nd closest OM to target.
        om3 (float): Distance in km of 3rd closest OM to target.
        omd (float): Distance in km between adjacent OMs on planetary body.

    Returns:
        leg1 (float): Distance in km of 1st leg (OM1 -> OM2)
        leg2 (float): Distance in km of 2nd leg (OM2 -> OM3)
        leg1r (float): Distance in km to OM2 after travelling 1st leg
        leg2r (float): Distance in km to OM3 after travelling 2nd leg
    """

    # Calculate leg length using OM pathing formulae
    leg1 = (om1**2 + omd**2 - om2**2) / (2*omd)
    mid = (omd**2 + leg1**2 - omd*leg1)**0.5
    leg2 = (omd**2 - omd*leg1 + om1**2 - om3**2) / (2*mid)

    # Calculate remaining distance to OMs after travelling leg
    leg1r = omd - leg1
    leg2r = mid - leg2

    # Round all values
    leg1 = round(leg1, 1)
    leg2 = round(leg2, 1)
    leg1r = round(leg1r, 1)
    leg2r = round(leg2r, 1)

    return leg1, leg2, leg1r, leg2r
